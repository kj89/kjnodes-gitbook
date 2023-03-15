# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)




## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:20090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:20656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:20659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (20)
```bash
peers="94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30582,27238e2f804bf28a14c186a2e0f0ceaae0d2588f@176.9.98.24:30590,dee24c88c902ae0b117141f3b1e696b5c92d8e51@57.128.74.73:26656,a1a3fa715c6bc4257613cfbdec06e7d9a0e1edee@65.108.134.175:26656,2b8f5b788108c593378ce0dad8faff180b854cb4@185.56.139.86:26656,02c88d98245ec8b06546f6b19866b758f2df2c6e@95.217.194.249:26656,a1e08e481992149d50cb74144602334e71fa3aa3@62.232.97.106:26656,68a87c501de64b9259a0023d20fb805dff89082e@13.58.18.103:31380,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,02241bb63c01fb52033029f7155c3db5d7846c1f@168.119.64.26:26656,cc167c48a977160de9f9bbb5c3b80ddb7d585a67@176.9.156.135:26656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,02b93545950853d692d7ea63eac879e6dd4bf390@82.223.122.139:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,d78275c79f81efc0eb357cec3ec35877efec4974@57.128.74.131:26656,6f3d14f3ca7bb06e6ba560ab78e70aa77c0ca0d0@65.108.99.238:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,6df4a6d0db5a771b84055646fe3814c655dd3428@95.216.163.64:26656,572cb08735d4572fe62b2fc8b9555c479d8e162f@65.108.137.217:26656,b937814a2ddd889a9a72aaf48d013a47f98721ee@217.160.39.214:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
