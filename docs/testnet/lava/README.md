# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.9.8 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

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
peers="5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,1550fe479ee2dcfa35f7dcd2c66f37a50d34b0e3@178.63.132.243:2237,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,d64aa8f4d864daac54639cd1fdebbf4c464ba4f1@5.75.235.206:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,a5637262d92b9c503d6abbb181d58a2314f67e1d@84.46.243.129:26656,3456c9ba0df46cbb526717d73fa51ff0ed9a53a1@95.216.14.58:60756,92638cc11f41a91cdf86d3e1b21c2396d82bcc4a@95.216.26.91:26656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,ff27ef7b864955c912281d307c85d4ac9f9b9f54@159.223.64.76:26656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,b05087fe1d35652de94643a229d53f8fef9c19e2@5.189.128.140:26656,1bbcf26a68705396f2e36593a585c64a1fd761bf@38.242.193.117:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
