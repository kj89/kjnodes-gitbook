# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (14)
```bash
peers="360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,35d1047d50226c8dd42f2402c212f92bf7935108@65.109.112.20:11164,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,00cedd85b1f6a2c859a8c6116b9578e1cc2623c6@51.222.44.116:30656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
