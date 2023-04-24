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

**live-peers** (29)
```bash
peers="161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,ee14b4bbeb436056952c8e4e7c84826dfb92143b@65.109.105.17:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,be4ff5b09936e32d9a4f87f5a5118973160d58f2@78.47.214.204:26656,679f56feb7f4f91d46a92d0eb474d1dc43466d18@213.239.215.59:29986,e1a24aaba30a8ff21e52fed92b96b36156b52e80@51.161.208.88:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,1c3db399f804a111efebeeffb5cdc4e751fb8108@65.109.61.113:21609,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,908a73baeebf599fad2c8a05a6e025eee2ee9ee0@212.23.222.26:36656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
