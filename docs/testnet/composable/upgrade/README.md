---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: banksy-testnet-3 | **Latest Version Tag**: v3.0.3-testnet | **Custom Port**: 159

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf composable-testnet
git clone https://github.com/notional-labs/composable-testnet.git
cd composable-testnet
git checkout v3.0.3-testnet

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.banksy/cosmovisor/upgrades/v3/bin
mv bin/centaurid $HOME/.banksy/cosmovisor/upgrades/v3/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
