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

**live-peers** (27)
```bash
peers="e5e71ccd387eba74fec51b211e9236fca965af40@46.4.5.45:11556,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,b7084c40af131f24ab7e449a9844e0f56c94fa41@51.91.30.173:4000,c0d0c9f1ef645bcf1c214b05581c9d4a4b45e97e@185.230.138.96:26656,8b96338b18c1e4a76a119fe0812c131a4e2cc96a@65.109.70.45:20656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,72ff166996ef9590879a7b7ab00b3b71529632a9@65.109.90.171:31656,0010101912f896d44bc735b01741de9314953d79@93.78.208.38:26656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,958d9056c6173edb4714b6468bda509e97d0c80c@65.108.231.124:45656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,0cf5d2bcc49c1acddb6b7b2bc547543ec2fbe844@34.239.246.206:26656,e50d7fa6a50ac792e5df61ff621d9621e9fcc8aa@34.133.135.231:26656,b6031525e988eefd03452807806f08b0e9bc3289@15.235.46.50:26656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,900950a031cb758b761198e52b07fcc17616bd76@65.21.200.54:40656,20355d8c6b7e8c77576982bfca148b5cbd1a538d@185.230.138.95:26656,11aa4b7b17ac0a3372e98d4cbf83aacd6cfbbfdd@1.54.176.18:15656,883e6d6e78f04be2cc7ac81f26e155de6103adf6@77.51.200.79:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,8b728546d0e0e422c1cd9e9f9cb6a3e67ac3e86d@184.174.37.152:15656,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,874f0042c20d3808eccb86b523fffe42903034b8@95.217.144.107:11556,bce4a3976c39d811d50b18ed104b0d04da398591@213.239.207.175:53656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:26946"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
