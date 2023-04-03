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

**live-peers** (31)
```bash
peers="ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,4aa6607f87ad0b458526d3405731e71553cf275c@219.100.163.35:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@65.108.231.124:15656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,05241d21ff9e7c699bbdb4faa73da1860b6d8cd7@128.199.85.168:26656,4ff179ec503516c869e4104bc0af85e324deefb2@46.101.75.31:15656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,663134c4999f4f9fc59879eaaebbb332e91e2160@45.34.1.114:33656,9bed2c944243fd3ee35a6e4e8da0956f61518603@65.109.21.75:26656,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,29b915115d1bca2c7242b08849c76658c21a136b@146.59.118.31:32182,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,914bed178748772d7578d119cb2dc89d5076b9f4@135.181.223.115:2390,a1f5e0b68f36091d5fc8f30aba914b6c191f21fa@65.108.128.201:11156,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@172.111.52.50:32662,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
