# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="7a9cd31ca48252a741ef0689bc35b751bffd555c@89.117.49.164:26656,577e5876fab3d5f94a43522a58f2fe0f07445599@95.217.211.32:30656,349d92de7d6e23ff4ce6dfbf6628a04da3483245@194.163.155.195:26656,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,bd798e85f2e58cd0da70e6266014841dd79aaf04@65.109.160.90:18656,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,c38634d727ec644530dff5a8dfe11ee45f9ae735@95.214.53.218:11656,77ae41601b06b3ca611e51047df04d3e35908aff@5.78.79.229:18656,4ed3e9ac9d276b6f47e13eca99dc0f184e6b9c0b@185.249.225.160:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
