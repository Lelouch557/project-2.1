#include <avr/io.h>
//#define F_CPU 16E6 -> Dit moet wel als je Visual Studio gebruikt
#include <util/delay.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <avr/interrupt.h>
#include "AVR_TTC_scheduler.c"

// output on USB = PD1 = board pin 1
// datasheet p.190; F_OSC = 16 MHz & baud rate = 19.200
#define UBBRVAL 51
int time_to_go_up_or_down = 1;
int stateofscreen = 0; // UP state
static volatile int pulse = 0;
static volatile int integer = 0;
static echo_pulse_time = 15;
static uint8_t red = 0b00000100;
static uint8_t yellow = 0b00001000;
static uint8_t green = 0b00010000;
int automatic_state = 1;





// Putchar tbv. stdio.H
// bron: https://www.nongnu.org/avr-libc/user-manual/group__avr__stdio.html


static int ser_stdio_putchar(char c, FILE *stream) {
	if (c=='\n') {
		ser_transmit('\r');
	}
	ser_transmit(c);
	return 0;
}

static FILE uart_output = FDEV_SETUP_STREAM(ser_stdio_putchar, NULL, _FDEV_SETUP_WRITE);

void ser_init() {
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	UCSR0A = 0;
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
	stdout=&uart_output;
}

void setup_timer(void){
	DDRD = 0b11111011;
	DDRB = 0xff;
	EIMSK = 0b00000001;//enable interrupt0
	EICRA = 0b00000001;//setup to generate interrupt request at any logical change
	TCCR1A = 0;
}

int readADC(uint8_t ADCport)
{
	// use ADC port
	ADMUX = ADCport;
	ADMUX |= (1 << REFS0);
	ADMUX &= ~(1 << ADLAR);
	ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
	// Enable ADC
	ADCSRA |= (1 << ADEN);
	// Start ADC conversion
	ADCSRA |= (1 << ADSC);
	// wait for ADC to finish
	while(ADCSRA & (1 << ADSC));
	int ADCvalue;
	ADCvalue = ADCL;
	ADCvalue = (ADCH << 8) + ADCvalue;
	//return ADCvalue
	return ADCvalue;
}
void ser_transmit(uint8_t data) {
	loop_until_bit_is_set(UCSR0A, UDRE0);
	UDR0 = data;
}
void up(){
	int amount_of_sec = time_to_go_up_or_down * 20;
	int bool = 1, counter = 0;
	if(stateofscreen == 1){
		stateofscreen = 0;
		while(counter < amount_of_sec){
			if(bool == 1){
				bool=0;
				PORTB = red;
				}else{
				bool=1;
				PORTB = red + yellow;
			}
			counter++;
			_delay_ms(500);
		}
		PORTB = red;
	}
}
void down(){
	int bool = 1, counter = 0;
	if(stateofscreen == 0){
		stateofscreen = 1;
		counter = getDistance();
		while(counter < 20){
			if(bool == 1){
				bool=0;
				PORTB = green;
				}else{
				bool=1;
				PORTB = green + yellow;
			}
			counter = getDistance();
			_delay_ms(500);
		}
		PORTB = green;
	}
}
void ser_write(char *s) {
	int i=0;
	while (s[i]!='\0') {
		ser_transmit(s[i++]);
	}
}

void ser_writeln(char* s) {
	ser_write(s);
	ser_transmit('\r');
	ser_transmit('\n');
}

uint8_t ser_receive() {
	loop_until_bit_is_set(UCSR0A, RXC0); /* Wait until data exists. */
	return UDR0;
}

void ser_readln(char* buf, int maxlength, uint8_t echo) {
	int i=0;
	while(1) {
		uint8_t c = ser_receive();
		if (c=='\r') {
			break;
		}
		if (i<maxlength-1) {
			buf[i++]=c;
		}
	}
	buf[i]='\0';
}
int ser_read() {
	uint8_t c = ser_receive();
	return c;
}
void showNumber(int value){
	char str_buf[20];
	sprintf(str_buf,"%d", value);
	ser_write(str_buf);
}
int16_t getDistance(){
	int16_t count=0;
	uint8_t temp = PORTB;
	sei();
	PORTB |= 0b000000010;
	_delay_us(echo_pulse_time);
	PORTB = temp;
	_delay_ms(100);
	cli();
	count = pulse/1000;
	return count;
}
double get_Temp(){
	double ADCvalue = readADC(3);
	
	double temp = (double)ADCvalue / 1024;   //find percentage of input reading
	temp = temp * 5;                     //multiply by 5V to get voltage
	temp = temp - 0.5;                   //Subtract the offset
	temp = temp * 100;
	return temp;
}

double get_light(){
	double ADCvalue = readADC(1);
	
	double temp = (double)ADCvalue / 1024;   //find percentage of input reading
	temp = temp * 5;                     //multiply by 5V to get voltage
	temp = temp * 100;
	return temp;
}
void loop(){
	char in_buf[30];
	int16_t count = 0;
	ser_readln(in_buf, sizeof(in_buf), 1);
	_delay_ms(50);
	
	if(strcmp(in_buf,"LIGHT") == 0){
		//LICHTSENSEOR
		showNumber(get_light());
	}

	if(strcmp(in_buf,"TEMP") == 0){
		showNumber(get_Temp());
	}
	
	if(strcmp(in_buf,"DISTANCE") == 0){
		count = getDistance();
		showNumber(count);
	}
	
	if(strcmp(in_buf,"DOWN") == 0){
		down();
	}
	if(strcmp(in_buf,"UP") == 0){
		up();
	}
	ser_writeln("OK");
}

int main() {
	setup_timer();
	ser_init();

	DDRD = 0b11111011;
	DDRB = 0xff;
	PORTB = red;
	
	ser_writeln("SETUP DONE.");
	
	SCH_Init_T1();
	SCH_Add_Task(loop, 0, 1);
	SCH_Start();
	while (1) {
		SCH_Dispatch_Tasks();
	}
}

ISR(INT0_vect){
	if(integer==1){
		TCCR1B=0;
		pulse=TCNT1;
		TCNT1=0;
		integer=0;
	}
	if(integer==0){
		TCCR1B = 0x01;
		integer=1;
	}
}
