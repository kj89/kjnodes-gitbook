# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-3 | **Latest Version Tag**: v0.5.2 | **Wasm**: ON

[Website](https://archway.io) | [Discord](https://discord.gg/archwayhq) | [Twitter](https://twitter.com/archwayhq)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/archway-testnet](https://explorer.kjnodes.com/archway-testnet)

## Public endpoints

* api: [https://archway-testnet.api.kjnodes.com](https://archway-testnet.api.kjnodes.com)
* rpc: [https://archway-testnet.rpc.kjnodes.com](https://archway-testnet.rpc.kjnodes.com)
* grpc: archway-testnet.grpc.kjnodes.com:15690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json
```

**live-peers** (26)
```bash
peers="e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,f7a7c6bf673c201c55ecf0d249df43826293d9d4@176.9.28.41:26656,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,7f46c5c86639e04183cea341d62c59213cdc4542@185.230.138.49:26656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,d1334258b592ebccb85a917aa65976b74e254a60@65.109.65.248:31656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,72ff166996ef9590879a7b7ab00b3b71529632a9@65.109.90.171:31656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,c0d0c9f1ef645bcf1c214b05581c9d4a4b45e97e@185.230.138.96:26656,a03c1958163dc7d3035214b67bf4734801cd482a@138.201.204.5:50656,05413d5814b6efbb1cddec9ae240b2c638a127f5@222.106.187.14:53100,ac7e3903648ea720a8c3a8fec4051f8fabbc79cf@185.185.82.252:26656,1413664d3cfa37c2d661f740b2b47105433f3872@65.21.139.155:34656,11aa4b7b17ac0a3372e98d4cbf83aacd6cfbbfdd@1.54.176.18:15656,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,900950a031cb758b761198e52b07fcc17616bd76@65.21.200.54:40656,bce4a3976c39d811d50b18ed104b0d04da398591@213.239.207.175:53656,147c1668031ee62a85bd7293a845fdcf4f7b1857@222.211.225.0:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
