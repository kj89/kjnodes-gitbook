# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.6.0 | **Wasm**: OFF

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

**live-peers** (42)
```bash
peers="dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,fdc3bd914360b1be8ee2e9f4a447223830527497@78.46.36.203:26656,d4cc923616adf5728f6383bcef408b8954ccfbd8@138.124.184.204:26656,c69864d1c6dd7132f2f65eafec6e6828938c5c8d@37.221.198.252:26666,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,8a089094624f27698f365402a059b8b810532805@207.180.229.129:26656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,1598a86c04a64d17fa15a07eb201f50c5d760842@75.119.136.106:26656,e268a2ce255d51a93e6ec89ee73c233bbaec70f4@49.12.185.46:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,474e2436e097c28472a1fe269e1825762fa340d6@38.242.128.19:26656,c5c98017339ce6d4d5d2a4fd0fb1aaeb966ef0f7@65.108.124.57:36656,944389dd08321247c8ad687d904591a3d73d16c6@173.249.38.130:26656,877fb1670209bc2a347d7755388b677b330e98ea@95.216.9.42:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,c83d7b205b2e80bd9a33c13161bd39d520988455@38.242.139.189:26656,d5ad7ae6caf54ef20a6dc04d30a55caac6c540c9@5.61.41.138:26656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,bec79fab73dbbe345d8b26cdeeeee4ab83fdf80e@176.9.22.117:35656,e83c0fdeb2b0e258bb559d657d0907b63635127a@159.69.149.85:26656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656,aa5c52f79bdf256a5581b8fd396e2180fb523b2c@178.18.247.249:38656,94bba76f57bc30a6c0afa4ca10cd54d0b247569d@38.242.221.85:26656,5e8d65796d939fc16fa0c955dfbd16c9c519606b@222.71.35.43:26656,1a0dc31600f1f9d0664f3307a7d38b240722569c@64.176.4.130:44656,2cb465a7c919321978f89701b4ae07ac505f7ad8@194.163.184.228:26656,ade02cddf71489b79a2054a7c6ba2cab8a0abb18@185.163.125.232:26656,6f1f1414c63e9ffca9cb59fe4c847580da2020d6@109.123.235.222:10104,3da3c50af9ee93819912c63a386e30dde70a1518@213.136.73.17:26656,1550fe479ee2dcfa35f7dcd2c66f37a50d34b0e3@178.63.132.243:2237,df4a126e75dac4e7e2c4c7ea451a547c337a9f2a@46.4.253.147:26656,f00678dae0448ca33974a359bb1986e52b7ac19f@43.153.32.148:26656,cba6347ac83120324c34514d383f3e9835ac15e9@5.75.139.114:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:33256,61c9667630221059a971a114e48a936f45084d2e@185.209.230.156:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
