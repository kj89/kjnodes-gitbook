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
peers="e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,780b02fd73b698834c4cdd0c7d7123586b71ece1@209.38.243.102:18656,2716bf898b87093e46d383e9be512671d4f6a05a@65.108.87.179:18656,f55eaf24fe87dfe4c5feb64ba2e2f5b730901927@185.255.131.190:26656,4a1da7aeb094d01f75970c1115e71222617777f4@135.181.249.140:18656,bd798e85f2e58cd0da70e6266014841dd79aaf04@65.109.160.90:18656,b5ba578a3a3b50fc551ecfecd80811eaddd0a2e6@109.123.240.165:34656,d10fae49b6fa0a3dbfdca205807f79b3d53ece98@94.103.92.112:26656,30408b285f4989484dff0a273d5221c583e5eff3@164.92.82.243:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
