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

**live-peers** (41)
```bash
peers="306ce653d6f0c77936b681d4ee8bbf66a4b8bb75@88.208.57.200:60956,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656,e6dcff84fa8e853372499feb8d0d739d9ca41c96@195.201.241.25:35656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,4990ed7074424046184dd474df40902c30f34182@65.108.250.241:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,24da98830276fb0b4fc209cfcaf0cc3a287e1bdd@135.181.222.179:26656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,064fe9fe19fe5552b2d4922d659466e583f42b22@95.216.2.219:26658,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,bc777df96c83c0433561c88c541dbbc520928f6c@195.3.221.239:26656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,3e982cadd9956384478798f8ab1a686632be0fd4@149.102.156.102:35656,1a395e1ce2119531b831c4b9979718dd810f0244@195.46.164.179:31656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,ff6df373bf7bce436d488d2d8f5f5b283c6431d4@51.79.100.160:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,f1b1df46afd4c9d4f66051437078c0b85bc6b67b@65.108.206.118:61056,d43289f43e6fba3aaa51559d35b377907dd12007@65.108.234.11:11656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,acba49be707c31a831a3bca9d9d9f7defcc0bd21@142.132.148.174:26656,5a223d77d01319a8c7f648eddfc8549cafcd8ca5@34.147.118.211:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656,f701c2bbd3ec1202eb3af17242ddec853ab9f5d9@84.46.242.147:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
