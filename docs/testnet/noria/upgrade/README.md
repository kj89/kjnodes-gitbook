---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/noria.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: oasis-3 | **Latest Version Tag**: v1.3.0 | **Custom Port**: 161

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf noria
git clone https://github.com/noria-net/noria.git
cd noria
git checkout v1.3.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.noria/cosmovisor/upgrades/v1.3.0/bin
mv build/noriad $HOME/.noria/cosmovisor/upgrades/v1.3.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
