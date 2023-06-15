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

**live-peers** (11)
```bash
peers="b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,6e2dac7a826fa2c21867dc6620b5945574a89865@65.109.155.238:29656,b1f13e9971cfdcf784fb0efbd1b72417d5410a02@195.201.59.194:26656,f8ae768832a2665c915c3965a5bb8dc1031d5c1e@46.4.23.42:16656,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,fd6bccda6c8c16ed694c1f447966202492a3945c@65.108.72.253:26656,3563bf0924f203b6b7c5e31c21c1de4a8f2e0949@178.23.126.92:26656,4a6451353a1040ccb2638de485feda28d40416cd@65.109.84.103:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
