# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```bash
peers="dea00215e54c4098a4f194a7ecd43e24ea99336f@88.99.95.81:26656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,182a0faf787f0f62ac2af8975d951ab94573d7d2@194.195.87.52:41656,1fee6e7fd077911abab93739f6bf13c62dedbf20@178.62.204.49:26656,c78af3c8a2fa3d398dedb1ad9052eaf60dc27434@95.216.163.254:41656,33196fb0090d2de3671e36545d3425f641c9c0dc@65.109.70.4:41656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,6c938c9a9aeb2d6ab5f3c3695221a408f467a5d4@176.57.188.138:41656,4ec16520a171af24269ddb7aa57f555a455bc76d@95.111.247.144:26656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,921348b18868c83bfc5375fc9860bb28aaaf0d0e@38.242.238.229:26656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,c5fa8b2df54c71b7a6479d9ba67dcd87b7109f25@103.104.75.230:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,b5fbf2633a1d00c4e0e62f1e0012f8e72af15aa9@185.218.124.169:26656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,6ce7f9ea8e3019c50057f4eb2a0ed55e8eedf874@194.50.0.44:26656,df66a0896a1f6cac3ad45810346c1d096b42adc9@164.92.80.120:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,926b47f8d786e544ec3a9200c61b5b04729a9d57@199.175.98.127:41656,e704537ce1348bfc7b781d6546ae272ff3eea8d5@34.117.96.202:26656,edae8278cef6113e38af80504fb83cbf5eb0f023@165.232.129.242:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,74a4bbfbf4d1ca9852d10f3a97e4d012c62aec9e@146.190.102.111:41656,d312ba9da73e07c88918c56908e84ba28907808a@65.108.69.68:26858,200b0594c8bfd86c1fc2a5b5c72e266139f3b193@62.171.140.239:26656,975a3ade04fc92d00c7ad59d536506fde46169e7@167.86.96.233:656,5b599e2470b01f8afa88448899f436130fb2e2fd@146.190.112.167:26656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,ae5d5b47ea732ff509114f405967f61eb3d86ac6@75.119.146.171:656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
