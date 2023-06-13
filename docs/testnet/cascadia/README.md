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
peers="b71287a85b70df75e1405c6831634738e6b957ab@65.108.72.253:15656,bcd8376ebaad3582d3b2d06d1ca35286b5df6df8@65.109.48.181:27656,8274413c90f8f34ccdd35c0f3a59d546d8abbcbb@155.133.22.40:26656,d417eb06db1da1790b2a9238630731ec6ca9eeb5@91.142.72.79:26656,7d63f71ab6356940c607d9d748262b5505b604b0@49.12.42.105:26656,d663b2312b55df2a3637608ee470e9610b9fc7ae@5.231.208.215:26656,6b4f8c1113823200d0711e673824654060b3f008@84.46.242.124:55656,97a5c1de5dc145baf35e92ad56cd8015a3d4c2bb@45.10.154.249:18656,881418c296ee6744b7ac5ffa73441aa46ae0171b@155.133.27.235:26656,6f44ab7ad9d6a4366a80c8fd8f904e6ab2f6e535@5.9.48.90:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
