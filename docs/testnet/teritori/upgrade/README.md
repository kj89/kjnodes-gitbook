---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: teritori-testnet-v3 | **Latest Version Tag**: v1.4.0 | **Custom Port**: 119

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf teritori-chain
git clone https://github.com/TERITORI/teritori-chain.git
cd teritori-chain
git checkout v1.4.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.teritorid/cosmovisor/upgrades/v1.4.0/bin
mv build/teritorid $HOME/.teritorid/cosmovisor/upgrades/v1.4.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
