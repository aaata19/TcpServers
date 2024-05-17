#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>

#define PORT 8413
#define SHIFT 3

void caesar_encrypt(char* message, int shift) {
    char c;
    for (int i = 0; message[i] != '\0'; ++i) {
        c = message[i];
        if (c >= 'a' && c <= 'z') {
            message[i] = (c - 'a' + shift) % 26 + 'a';
        } else if (c >= 'A' && c <= 'Z') {
            message[i] = (c - 'A' + shift) % 26 + 'A';
        }
    }
}

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char message[1024] = {0};
    char buffer[1024] = {0};

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }

    for (int i = 0; i < 5; i++) {
        printf("Enter message: ");
        fgets(message, 1024, stdin);
        message[strcspn(message, "\n")] = 0;
        caesar_encrypt(message, SHIFT);
        printf("Encrypted message: %s\n", message);
        send(sock, message, strlen(message), 0);
    }

    read(sock, buffer, 1024);
    printf("%s\n", buffer);

    return 0;
}