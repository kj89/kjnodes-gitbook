# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v2.0.3

Website: [https://stride.zone](https://stride.zone)

## Public endpoints

* rpc: [https://stride.rpc.kjnodes.com](https://stride.rpc.kjnodes.com)
* api: [https://stride.api.kjnodes.com](https://stride.api.kjnodes.com)

## Public peers

### state-sync

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:16656
```

### seed-node

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659
```

## Restake

[Restake with kjnodes](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n) (every day at 08:00, 20:00)
## Address book
```
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

## Live peers (10)
```
PEERS="23180f90318d0003a4e8140a1e67407bf874d69d@78.107.234.44:25656,1f78bdc1c2e2268185dac25fa076f743d8bbd154@95.217.109.143:56656,d13d51e660dbd89d6660ac9b61957c5e727efdae@135.181.130.145:6000,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,c4688bb34164eacacaa374bc7440b87986dd87ac@162.251.235.252:26656,b234b84e0c950b0377bec9c16d86f0adb1f3f9ef@176.9.155.55:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656,04ea9eceee16db90872fee3fbef9ac50a87702c5@185.248.24.29:26656,64920ef07c20c22f26a2164ceae2aac60ec2840d@95.216.73.250:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$PEERS'"|' $HOME/.stride/config/config.toml
```
