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
peers="61d96fee29a9615c208c4db72526d23b45094cb4@65.108.195.30:36656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,271419d3eb3878c902ebb0064490ad702d9d067f@144.76.145.150:26656,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,1c3db399f804a111efebeeffb5cdc4e751fb8108@65.109.61.113:21609,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,2020c09ef7542899a4c55b382013c469122186d6@51.195.88.136:15620,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,e8273dbc72d6ec93048e9ee0d428c658ddf99077@75.119.144.167:26656,618e09601dd5abb2bd02de957982742e4c1975ab@195.14.6.2:26656,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
