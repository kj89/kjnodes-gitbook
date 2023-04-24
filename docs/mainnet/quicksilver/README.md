# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.9-hotfix.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,71d1e3336f41475c3dfc247aa77a8842a24c369a@144.91.80.32:11656,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,3364e9309e464ef9a8fb434db6a47168546f7f91@139.99.208.77:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,2b73e89e8b8ff83271665a9766eba76dcd15735f@57.128.73.31:32306,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,34047b39deae3110158c2bf7359e4a1b559dd8ca@159.89.171.207:26656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
