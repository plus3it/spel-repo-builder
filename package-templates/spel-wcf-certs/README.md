# spel-wcf-certs

Provides a package to install and update DoD WCF CA certificates.

# How to Update WCF_CAs.pem

DISA periodically releases a new WCF CA bundle. These bundles are published here:

* <https://public.cyber.mil/pki-pke/>

Notifications of updates to the bundle go out via the "Tools" RSS feed:

* <https://public.cyber.mil/pki-pke/rss-2/>

When a new bundle is published, follow these instructions to update `spel-wcf-certs`:

1. Download the new bundle and extract it
2. Identify the `*pem.p7b` file in the bundle
3. Run this command to export the CA certificates to a concatenated PEM file:
    ```
    openssl pkcs7 -in *.pem.p7b -print_certs -out WCF_CAs.pem
    ```
4. Create a new branch in this project
5. Replace the `WCF_CAs.pem` file with the new version
6. Update `spel-wcf-certs.spec` with the new version and a changelog entry
7. Commit the change and open a pull request
