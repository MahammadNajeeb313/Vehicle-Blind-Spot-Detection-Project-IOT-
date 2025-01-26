#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

// WiFi credentials
const char* ssid = "SSID";       // Replace with your WiFi SSID
const char* password = "Password"; // Replace with your WiFi password

// Web server on port 80
ESP8266WebServer server(80);

const int buzzerPin = 14; // GPIO14 corresponds to D5 on NodeMCU

void handleBeep() {
  // Turn the buzzer on
  digitalWrite(buzzerPin, HIGH);

  // Send a response to the client
  server.send(200, "text/plain", "Buzzer is beeping for 1 seconds!");

  // Delay for 5 seconds (buzzer on)
  delay(1000);

  // Turn the buzzer off
  digitalWrite(buzzerPin, LOW);
}

void setup() {
  // Set the buzzer pin as output
  pinMode(buzzerPin, OUTPUT);
  digitalWrite(buzzerPin, LOW); // Ensure the buzzer is off initially

  // Start serial communication
  Serial.begin(115200);
  Serial.println();

  // Connect to Wi-Fi
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Define the API endpoint for the web server
  server.on("/beep", handleBeep);

  // Start the web server
  server.begin();
  Serial.println("Web server started!");
}

void loop() {
  // Handle client requests
  server.handleClient();
}
