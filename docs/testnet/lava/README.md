# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)




## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (30)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,6f1f1414c63e9ffca9cb59fe4c847580da2020d6@109.123.235.222:10104,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,f00678dae0448ca33974a359bb1986e52b7ac19f@43.153.32.148:26656,c69864d1c6dd7132f2f65eafec6e6828938c5c8d@37.221.198.252:26666,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,f0679f7ee5038bb29d7cf1b823a44d6539484184@107.175.179.100:26656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,8a089094624f27698f365402a059b8b810532805@207.180.229.129:26656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,fdc3bd914360b1be8ee2e9f4a447223830527497@78.46.36.203:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,1598a86c04a64d17fa15a07eb201f50c5d760842@75.119.136.106:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,c83d7b205b2e80bd9a33c13161bd39d520988455@38.242.139.189:26656,2cb465a7c919321978f89701b4ae07ac505f7ad8@194.163.184.228:26656,40f008240242afc74b9531a87ce56e6a00221439@94.250.203.53:28656,d8a435d45d78afe849e8abec38cb5e9b9d9bbcd3@161.97.91.203:26656,877fb1670209bc2a347d7755388b677b330e98ea@95.216.9.42:26656,0064c6e0d31cd4059a49b185aa6048d79db391e1@109.123.241.244:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,a0476bc75ad2ade9ce8a6b2cd41ef646d3a2e3ee@85.10.193.246:28656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,30da6072679c936f66c07ae022191e9541027d1d@116.203.186.209:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
