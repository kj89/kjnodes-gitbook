---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.7.0 | **Custom Port**: 153

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf elys
git clone https://github.com/elys-network/elys.git
cd elys
git checkout v0.7.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.elys/cosmovisor/upgrades/v0.7.0/bin
mv build/elysd $HOME/.elys/cosmovisor/upgrades/v0.7.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
