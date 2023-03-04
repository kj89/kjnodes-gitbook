---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.5 | **Custom Port**: 40

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf defund
git clone https://github.com/defund-labs/defund.git
cd defund
git checkout v0.2.5

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.defund/cosmovisor/upgrades/v0.2.5/bin
mv build/defundd $HOME/.defund/cosmovisor/upgrades/v0.2.5/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
