import validators
import whois

#ask user for domain details and verify domain.
while True:

    domain_name = input("Please provide the domain name: ")

    if validators.domain(domain_name) != True:
        print("domain name incorrect !!  please try again")
        continue

    break


print("checking domian registration status...... ")
domainstatus = whois.whois(domain_name)
print("you are using below name servers: ")
nsdetails = domainstatus.name_servers
for i in nsdetails:
    print(i)