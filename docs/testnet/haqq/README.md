# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)




## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: [https://haqq-testnet.grpc.kjnodes.com](https://haqq-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (37)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,e99d8010469441c82a69f6abcbd853174b450be1@149.102.156.103:35656,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,001eb7a3a03dc11539541737262c4ddc84dec283@91.195.101.98:26656,e576d332451c7c3c0c5c753b1bbd4e670b1ecfc7@5.161.97.83:26656,dd5ebfba86d8b5ff9c6ea3eb340fdb30e4c6990f@162.55.102.45:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,4990ed7074424046184dd474df40902c30f34182@65.108.250.241:26656,064fe9fe19fe5552b2d4922d659466e583f42b22@95.216.2.219:26658,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,ffc8b0dbe8eea3083320cdc014cc6ce8f60e5096@23.88.74.54:35656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,9f91d1845f0bd759ff6b83ba5e0f6f6650f57fa2@149.102.132.135:35656,04e76400e2ad0063e18a2174adad69853a13e8bc@149.102.133.20:35656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,50898046189f8cd8f7e996852ac84037c914a8ee@149.102.132.140:35656,70c1b8334bf08fe5d56fb53d07da11f01faa560b@65.109.30.90:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
