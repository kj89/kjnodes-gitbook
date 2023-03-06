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

**live-peers** (33)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,f0679f7ee5038bb29d7cf1b823a44d6539484184@107.175.179.100:26656,c69864d1c6dd7132f2f65eafec6e6828938c5c8d@37.221.198.252:26666,f00678dae0448ca33974a359bb1986e52b7ac19f@43.153.32.148:26656,11a19d02406bee18a39e782f606d710d353de428@210.75.253.161:26656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,e268a2ce255d51a93e6ec89ee73c233bbaec70f4@49.12.185.46:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,8a089094624f27698f365402a059b8b810532805@207.180.229.129:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,c5c98017339ce6d4d5d2a4fd0fb1aaeb966ef0f7@65.108.124.57:36656,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,fdc3bd914360b1be8ee2e9f4a447223830527497@78.46.36.203:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,6b1d0465b3e2a32b5328e59eb75c38d88233b56f@80.82.215.19:60656,2cb465a7c919321978f89701b4ae07ac505f7ad8@194.163.184.228:26656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,c83d7b205b2e80bd9a33c13161bd39d520988455@38.242.139.189:26656,e83c0fdeb2b0e258bb559d657d0907b63635127a@159.69.149.85:26656,8d16f025aa05391f9e54c9e51cb3f931028cd2de@193.187.88.18:26656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,94bba76f57bc30a6c0afa4ca10cd54d0b247569d@38.242.221.85:26656,877fb1670209bc2a347d7755388b677b330e98ea@95.216.9.42:26656,d5ad7ae6caf54ef20a6dc04d30a55caac6c540c9@5.61.41.138:26656,aa5c52f79bdf256a5581b8fd396e2180fb523b2c@178.18.247.249:38656,e5f324d671e8bba44cd8eef2cb5b6e46ccf4f95a@65.108.199.120:60756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
