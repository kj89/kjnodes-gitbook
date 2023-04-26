# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

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
peers="67c3cc1397d0a0f03a45d4cae6ff3380be7364f9@95.217.229.18:11656,d5a9c9ae08f0d30e36c8f64eca046fc52b00561e@65.109.92.160:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,618e09601dd5abb2bd02de957982742e4c1975ab@195.14.6.2:26656,a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.98:26656,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,1c3db399f804a111efebeeffb5cdc4e751fb8108@65.109.61.113:21609,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,d93d33f89477252e0c31702e308a08914a179be9@51.83.184.168:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
