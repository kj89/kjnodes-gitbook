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
peers="7d63f71ab6356940c607d9d748262b5505b604b0@49.12.42.105:26656,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656,1168af52cf36c68e2405b3041c8d53ed1ca169be@65.109.158.190:26656,8a5caaaad14a554d71a8765e71b9f61da099efe2@65.109.39.113:26656,956e1b99ceef18f53b12ec7a0db97c350a7457a7@5.161.81.115:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,5126c2904cf4d9ed9b2c6cd203fccbe3983229da@23.88.5.169:22656,09e827239851ba5231bcaa47bbfbbc38d8289460@65.108.148.131:18656,30408b285f4989484dff0a273d5221c583e5eff3@164.92.82.243:26656,40739dda0aa1fd152faecfd540ddb876481fa7b2@170.64.158.48:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
