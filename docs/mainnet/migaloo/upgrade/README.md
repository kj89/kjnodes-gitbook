---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: migaloo-1 | **Latest Version Tag**: v2.0.5 | **Custom Port**: 149

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf migaloo-chain
git clone https://github.com/White-Whale-Defi-Platform/migaloo-chain.git
cd migaloo-chain
git checkout v2.0.5

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.migalood/cosmovisor/upgrades/v2/bin
mv bin/migalood $HOME/.migalood/cosmovisor/upgrades/v2/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
