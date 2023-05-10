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

**live-peers** (11)
```bash
peers="4affb0923e1be1f18818db3ababe682c63f6a1e3@65.109.144.236:30656,035df68157b66066b00390d74c6d4f4895cb1ef9@95.217.155.184:26656,dd6836e921c1ddc7b87d8c3dd87929dab80a9aaf@77.105.138.110:26656,cd8db9754f4468021ee9aec018861763e29acf35@65.109.92.60:26656,a38780ac3e28a29244df0702d3c1d61fa407db40@165.22.248.185:22056,68185619744c394d6113da12f5a95609cb86d853@34.125.30.159:55656,d663b2312b55df2a3637608ee470e9610b9fc7ae@5.231.208.215:26656,70b14a1f519398d88dfb64d28adb1eb75c33e888@65.109.117.165:55656,f47667544d7d5b65f316ba5ab8fca2e81e8fe4f4@157.90.208.222:36656,a47973f2e731fc35ea0f1e2d115b51ee77b91827@109.123.249.188:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
