---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: nibiru-testnet-1 | **Latest Version Tag**: v0.15.0 | **Custom Port**: 39

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf nibiru
git clone https://github.com/NibiruChain/nibiru.git
cd nibiru

# Build binaries
git checkout v0.15.0
make build
mkdir -p $HOME/.nibid/cosmovisor/upgrades/genesis/bin
mv build/nibid $HOME/.nibid/cosmovisor/upgrades/genesis/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
