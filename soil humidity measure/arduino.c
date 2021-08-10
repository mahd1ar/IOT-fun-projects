// YL-39 + YL-69 humidity sensor
byte humidity_sensor_pin = A1;
byte humidity_sensor_vcc = 6;

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    // Init the humidity sensor board
    pinMode(humidity_sensor_vcc, OUTPUT);
    digitalWrite(humidity_sensor_vcc, LOW);

    // Setup Serial
    while (!Serial)
        ;
    delay(1000);
    Serial.begin(9600);
}

int read_humidity_sensor()
{
    digitalWrite(humidity_sensor_vcc, HIGH);
    delay(500);
    int value = analogRead(humidity_sensor_pin);
    digitalWrite(humidity_sensor_vcc, LOW);
    return 1023 - value;
}

void loop()
{
    Serial.print("Humidity Level: ");
    double percent = ((double)read_humidity_sensor() / 1023) * 100;
    Serial.println(percent);

    delay(10000);
}