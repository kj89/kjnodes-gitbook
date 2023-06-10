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
peers="946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,bc098ac0149a0a06701e29e4f7c79cac65c25c7f@162.55.173.57:26656,28aab35e28e06497a7f8fc1a7a50982557bf3b2d@78.46.64.59:26656,2685f8e77fec93c99a55f2adb13835a50124d04e@135.181.18.112:55686,5b92ede5e88c5029d6c7b3b360b9cf59051ce409@65.109.84.33:26656,6e2dac7a826fa2c21867dc6620b5945574a89865@65.109.155.238:29656,be5158df5152ec7e6a4eca04c89e40494d19927c@51.79.101.159:26656,945422039658c95372b0b4f45c24ec4a5f849206@38.146.3.209:26656,f8ae768832a2665c915c3965a5bb8dc1031d5c1e@46.4.23.42:16656,497886715ac23475f7428bd177b9fa53ff886a8d@78.46.80.79:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
