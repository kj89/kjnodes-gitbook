# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

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

**live-peers** (15)
```bash
peers="ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,ea0c590882f4fa490a4563e364d341e078ad138e@94.131.105.228:26656,e4d0c8cf6a3dbee8af43582bb14e6e1077028341@198.244.179.125:30170,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
