# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: ollo-testnet.grpc.kjnodes.com:13290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:13256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:13259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,80b1ad27820f58b49e7a5a68881f0248a6269e9b@65.108.132.239:15656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,7864a2e4b42e5af76a83a8b644b9172fa1e40fa5@52.8.174.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
