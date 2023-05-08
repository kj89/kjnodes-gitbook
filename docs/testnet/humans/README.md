# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-2 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

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
peers="8c3c25fa9cd6289d0342cf0e42916f381a1fd671@78.46.64.59:26656,86768c62c83fcdeb54514b33b33ab44fd9fa5c05@49.13.9.135:26656,62faee4c6224b3562d7123acea58180021c8b47b@162.55.173.57:26656,6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:22656,69a6d587d4bd0d9f37404dbc03029c6220bde175@81.30.157.35:19656,1c8629b474c9e0f0b24e81684992448963cf8d11@65.109.84.103:26656,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,8d5e7c030a4790b2caba38520d167c1ab2bc1244@51.79.82.138:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
