---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.0-alpha.11 | **Custom Port**: 37

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf canine-chain
git clone https://github.com/JackalLabs/canine-chain.git
cd canine-chain
git checkout v1.2.0-alpha.11

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.canine/cosmovisor/upgrades/alpha11/bin
mv build/canined $HOME/.canine/cosmovisor/upgrades/alpha11/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
