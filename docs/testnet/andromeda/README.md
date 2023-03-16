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

**live-peers** (18)
```bash
peers="91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,7fd9a427a03f0e8632d2ff4b6fe32e99e3151f04@23.88.71.247:31656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,35d1047d50226c8dd42f2402c212f92bf7935108@65.109.112.20:11164,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,cd529600bb3aa20795a18c384c0edae2eb2da614@161.97.148.146:60656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,4a369367f8ee97c976330f9be79da387d11a0340@65.108.194.44:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
