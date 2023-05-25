# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-31 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

[Website](https://humans.ai) | [Discord](https://discord.gg/humansdotai) | [Twitter](https://twitter.com/humansdotai)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/humans-testnet](https://explorer.kjnodes.com/humans-testnet)

## Public endpoints

* api: [https://humans-testnet.api.kjnodes.com](https://humans-testnet.api.kjnodes.com)
* rpc: [https://humans-testnet.rpc.kjnodes.com](https://humans-testnet.rpc.kjnodes.com)
* grpc: humans-testnet.grpc.kjnodes.com:12290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@humans-testnet.rpc.kjnodes.com:12256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@humans-testnet.rpc.kjnodes.com:12259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/humans-testnet/addrbook.json > $HOME/.humansd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="df5cb643d8aeade8ef288a3dd90e4fd8220954ba@162.55.243.211:36656,0ae23e03040dd3e3a6c3a2326c62a206f531d671@162.19.31.150:26656,907cb9da5d7d7182a80a6e38aad59bd067059bb3@65.21.200.54:26656,4a6451353a1040ccb2638de485feda28d40416cd@65.109.84.103:26656,650b54b9fed877f05e8f2fa9b1a046e5a601a7c9@135.181.138.160:26656,d792d994b50e546cef27f177f549090e6e41476f@69.197.6.24:26656,442c270ecf448899ff266899b3e8fd819456b52d@185.252.232.85:26656,36f956fa2fe317a5d3163d0b6c7b104e33aa62e9@103.180.28.79:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256,d70c9343af28023a78aceb653e885666c12fec3b@138.201.121.185:26687"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
