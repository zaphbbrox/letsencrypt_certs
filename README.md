# letsencrypt_certs

An agent-based check for Check_MK.

It queries the output from ```certbot certificates``` and gives the remaining days until a Let's Encrypt certificate becomes invalid.  

## Usage

Deploy the directory *local* to your Check_MK instance and place them in your *sites* directory underneath ```/opt/omd/sites```.
Afterwards deploy the plugin to your hosts where you want to monitor Let's Encrypt certificates. Usually you'll have to put the plugin in ```/usr/lib/check_mk_agent/plugins```.

Now Check_MK should find the check automatically.

### Default Values

Remaining days which will create a WARN: 30
Remaining days which will create a CRIT: 15

You can change these default values and their created state in WATO.