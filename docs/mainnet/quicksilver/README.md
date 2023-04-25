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
peers="fb1e7a989ff78f0bdd7828dc3ade95dcd67cd5d0@65.109.116.151:15656,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,55a79e1163cf88e531aa2359038982edfd7b1526@176.9.16.233:11656,0a3860f9d3c27b34910fe8660240ae55699b55c2@84.244.95.245:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,149a25417349d70f5e5127a5eb634dbfaf6e6c3a@142.165.207.19:56656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,ba52d6744d89cf66cf29d7663a21e1299d0f6744@74.80.183.130:26654,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.89.247.21:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
