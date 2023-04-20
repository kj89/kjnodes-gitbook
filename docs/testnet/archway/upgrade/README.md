---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: constantine-2 | **Latest Version Tag**: v0.4.0 | **Custom Port**: 56

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf archway
git clone https://github.com/archway-network/archway.git
cd archway
git checkout v0.4.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.archway/cosmovisor/upgrades/v0.4.0/bin
mv build/archwayd $HOME/.archway/cosmovisor/upgrades/v0.4.0/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
