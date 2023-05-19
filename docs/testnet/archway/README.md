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

**live-peers** (23)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,900950a031cb758b761198e52b07fcc17616bd76@65.21.200.54:40656,6b137e1df61936010ea30a354d8abd7010598e29@35.239.130.141:26656,b9ba5ae75fbdee6812d1aa53ff7154ed59938cbc@57.128.151.101:26656,05413d5814b6efbb1cddec9ae240b2c638a127f5@222.106.187.14:53100,9a5b41ac06b3c131ca6e4959a465d6bc0d103e66@88.198.52.46:11556,cc683ab0fda09a798c4d2b176266e5c0d7bc1939@185.52.52.30:46656,fc96980110a96ce6f60999650fef94aad673ead5@138.201.204.5:50656,7786f708c1851dd433a03f71ec3ff74d65895de7@34.31.130.235:26656,c0d0c9f1ef645bcf1c214b05581c9d4a4b45e97e@185.230.138.96:26656,2854e7247155c5c0c418de40ed168850b4c73c60@85.232.252.19:26156,7e31ab391f5b5756a75dc18b5275b609c81a34ee@34.122.164.239:26656,c96b16a81c780d840530c17fec6efd31b329c458@34.133.135.231:26656,857515ed6ab05e8e59f74e1050cb9e653e899cac@159.223.220.1:26656,274f62099d692e1e250e85cec4b63846a076bb72@116.105.102.88:26656,147c1668031ee62a85bd7293a845fdcf4f7b1857@222.211.225.0:26656,261acb73f483d1cace653cb54f7b8815f63b7e56@54.36.227.1:26656,3fa606cdc1ea323e19d7c09648a4f3666f0bc672@211.219.19.69:29656,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,c56bad24170d2a7fa4b6316cc08b2432cc0b0db1@5.78.80.25:26656,d82343cb3d168522c54c4ffbfd4415e9b467e806@23.88.51.134:46656,c3b04bd407d9d42ead33c2ea2b7045a156ed9c01@58.186.69.132:15656,c8171d5b90ea72992408f8cfcd3893256d22aabc@65.109.94.221:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
