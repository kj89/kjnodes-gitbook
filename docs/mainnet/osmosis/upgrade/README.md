---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Custom Port**: 129

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf osmosis
git clone https://github.com/osmosis-labs/osmosis.git
cd osmosis
git checkout v15.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.osmosisd/cosmovisor/upgrades/v15/bin
mv build/osmosisd $HOME/.osmosisd/cosmovisor/upgrades/v15/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
