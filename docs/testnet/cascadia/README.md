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
peers="77319825e184e924bd30c5bcd0a3dc0abf181f31@178.63.26.94:55656,10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656,e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,d3e72dc135fb4534ea5a787220f040bb03394d4a@65.109.235.92:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,21ca2712116138429aed3d72422379397c53fa86@65.109.65.248:34656,a38780ac3e28a29244df0702d3c1d61fa407db40@165.22.248.185:22056,e500ca28e37c1fcd7f7167a6fa35c90e8d0a78f5@185.182.184.191:26656,77f241dc899638b011dd7448ca7897879cb590e4@195.3.220.22:11656,5e00a5323aa21b54669be868f2d2ab1e9d581207@135.181.183.62:18656,d663b2312b55df2a3637608ee470e9610b9fc7ae@5.231.208.215:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
