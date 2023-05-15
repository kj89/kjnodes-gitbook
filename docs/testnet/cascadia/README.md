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
peers="6f44ab7ad9d6a4366a80c8fd8f904e6ab2f6e535@5.9.48.90:26656,d1469dbfc3becdf0ec1640d6812793f6d33a6eda@5.9.121.55:41956,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,9d403738d8538bbf59901756162d4a7a88c7b5df@185.105.91.171:26656,793f9456b853f0d36e8e9636dcad5cc27a169292@91.230.110.100:26656,10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656,b667b29140a06ee79044b7ba9d3e4e96ff6f5292@65.21.141.155:656,84371a3cbc4d68ba96f05fbeb612bf4739a483e0@5.231.220.71:26656,30408b285f4989484dff0a273d5221c583e5eff3@164.92.82.243:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
