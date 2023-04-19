---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.9.0 | **Custom Port**: 26

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Download project binaries
mkdir -p $HOME/.gravity/cosmovisor/upgrades/orion/bin
wget -O $HOME/.gravity/cosmovisor/upgrades/orion/bin/gravityd https://github.com/Gravity-Bridge/Gravity-Bridge/releases/download/v1.9.0/gravity-linux-amd64
wget -O $HOME/.gravity/cosmovisor/upgrades/orion/bin/gbt https://github.com/Gravity-Bridge/Gravity-Bridge/releases/download/v1.9.0/gbt
chmod +x $HOME/.gravity/cosmovisor/upgrades/orion/bin/*
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
