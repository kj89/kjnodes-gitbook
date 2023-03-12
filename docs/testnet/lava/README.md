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

**live-peers** (40)
```bash
peers="d83043d1e14156d78722877b6f449e93b46ce871@142.132.152.46:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,38093a87129f828125be65e8969bb7ede682b26c@38.242.197.134:26656,29095bea094a78e3396f32535fa3fc6df9484f66@65.109.139.182:20656,11d25deba9c655a7312716810e3975fe175ada01@5.161.58.198:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,34271a6f82d755777a3db02be39e575bf4ebd415@65.109.30.197:28656,509eaf8341cca511c8a3127affaae2251593d514@161.97.148.146:56656,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,92b2e2f59cbbb11c601919f058575fbc50cb73c6@65.109.183.202:26656,40046fe63bdaa9efde27707b0d3de0bf84fedf80@86.111.48.158:26656,51aeaa2c757989f720c904023c2dbedfc720f75e@23.88.5.169:27656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,b05087fe1d35652de94643a229d53f8fef9c19e2@5.189.128.140:26656,a2c7ca668cd602ea61f86e4f15094d9ae93c5868@44.193.222.140:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,91c02af6333972f222570a73f51feccda8a3ccf1@65.109.93.58:26656,0925c475208d8e338907383ab87a094ad03c478e@65.109.55.186:40656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,f4d6605ea7a9a88d2afaf6c2c13f00b77eb3239f@185.241.227.182:26656,74ce58215cecca7a96c946b3cad6bbc282df9fa3@80.76.235.194:7064,9383be92dbd468a28955fff34753c1df6e0fa638@92.204.242.211:26656,fcd5a8f4aebc4c7100573914b7974a35cd389963@5.9.69.253:20656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
