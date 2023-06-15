# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,85953732c4eb5165724ac6db331240ff0815daf1@1.15.104.210:26656,a537cc2879fc79401f6834aa6483fbb1dee18ef0@137.184.44.33:20156,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,b97375574f263a2a97e6646b99f6ea444306758c@93.170.47.119:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,df441066ddfa6bd955fbf98ebf478f4406ab1cbd@188.246.224.85:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,d3ac63ff921486f8aef1eba7870cae1d14c38633@1.15.146.92:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
