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
peers="a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,6053a39e67c6bae83430e354f53d99e160e4964b@65.109.28.177:28656,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,55a79e1163cf88e531aa2359038982edfd7b1526@176.9.16.233:11656,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,c764a288f1d36e7ca2c953378bb4fd6a0eed4091@141.95.65.73:11156,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,21d8608d89e51b9ff806846538a45aed2aa25063@95.214.53.105:44656,bdbb005129890e3b656841415b3b728d1e4529e6@176.9.155.98:26656,c0beca70dbd3ef5bb433f7aa280d56d2a150bbd3@95.214.52.144:26656,443ad7c991b2915b620673b10206c92e2b4040e0@173.67.177.120:26656,d36921a835076f6d87889793eb05a83099617221@202.61.240.122:26666,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,908a73baeebf599fad2c8a05a6e025eee2ee9ee0@212.23.222.26:36656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,4ff179ec503516c869e4104bc0af85e324deefb2@46.101.75.31:15656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
